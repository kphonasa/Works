import sys 
import os
import struct
import socket

#input argument: hostname, returns DNS query message
#call: create_DNS_query(<url>)
def create_DNS_query(hostname):
	packet = struct.pack("!H", 12049)  				# Query Ids (Just 12049, Can randomize if you want)
	packet += struct.pack("!H", 256)  				# Flags (0x0100, Recursive Query)
	packet += struct.pack("!H", 1)  				# Questions
	packet += struct.pack("!H", 0)  				# Answers RRs
	packet += struct.pack("!H", 0)  				# Authorities RRs
	packet += struct.pack("!H", 0)  				# Additional RRs
	split_url = hostname.split(".")
	for part in split_url:
		packet += struct.pack("B", len(part))
		for byte in part:
			packet += struct.pack("c", byte.encode('ascii'))
	packet += struct.pack("B", 0)  					# End of String (implies that there is no URL information ahead)
	packet += struct.pack("!H", 1)  				# Query Type
	packet += struct.pack("!H", 1)  				# Query Class
	return packet

def decode_labels(message, offset):
	labels = []						
	while True:
		length, = struct.unpack_from("!B", message, offset)
		if (length & 0xC0) == 0xC0:
			pointer, = struct.unpack_from("!H", message, offset)
			offset += 2
			t_labels = decode_labels(message, pointer & 0x3FFF)
			return labels + t_labels[0], offset
		if (length & 0xC0) != 0x00:
			raise StandardError("unknown label encoding")
		offset += 1
		if length == 0:
			return labels, offset
		labels.append(*struct.unpack_from("!%ds" % length, message, offset))
		offset += length

def decode_question_section(message, offset, q_count):
	DNS_QUERY_SECTION_FORMAT = struct.Struct("!2H")
	questions = []
	for _ in range(q_count):
		qname, offset = decode_labels(message, offset)
		qtype, qclass = DNS_QUERY_SECTION_FORMAT.unpack_from(message, offset)
		offset += DNS_QUERY_SECTION_FORMAT.size
		question = {"domain_name": '.'.join(map(str, qname))}
		questions.append(question)
	return questions, offset

def decode_answer_section(message, offset, q_count):
	DNS_ANSWER_SECTION_FORMAT = struct.Struct("!2HIH")
	answers = []
	for _ in range(q_count):
		aname, offset = decode_labels(message, offset)
		atype, aclass, time_to_live, data_length = DNS_ANSWER_SECTION_FORMAT.unpack_from(message, offset)
		offset += DNS_ANSWER_SECTION_FORMAT.size
		resource = struct.unpack_from('!' + data_length*'B', message, offset)
		offset += data_length

		if atype == 1:
			ip = '.'.join([str(c) for c in resource])
			answer = {"hostname": '.'.join(map(str, aname)),
						"TTL": time_to_live,
						"IP": ip}
			answers.append(answer)
	return answers, offset

#input argument: DNS response message, returns IP address
#call: decode_dns_message(<DNS response packet>)
def decode_dns_message(message):
	DNS_QUERY_MESSAGE_HEADER = struct.Struct("!6H")
	t_id, flags, q_count, a_rr, auth_rr, additional_rr = DNS_QUERY_MESSAGE_HEADER.unpack_from(message)
	qr = (flags & 0x8000) != 0
	opcode = (flags & 0x7800) >> 11
	aa = (flags & 0x0400) != 0
	tc = (flags & 0x200) != 0
	rd = (flags & 0x100) != 0
	ra = (flags & 0x80) != 0
	z = (flags & 0x70) >> 4
	rcode = flags & 0xF
	offset = DNS_QUERY_MESSAGE_HEADER.size
	questions, offset = decode_question_section(message, offset, q_count)
	answers, offset = decode_answer_section(message, offset, a_rr)
	if len(answers) > 0:
		result = answers[0]
	else:
		return 'NULL'
	return result['IP']


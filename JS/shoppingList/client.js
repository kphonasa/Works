$(function() {
var counter = 0;
// Step 1
// This code is executed when someone clicks the "Add Item" button 
// at the top right of the shoppi		  var itemHtml = "<li><span class.'item-check'></span><span class='item-text'>" + listItem + "</span><span class='item-remove'></span></li><br>ng-item
// -------------------
	$(".add-item").on('click', function(event){
		  event.preventDefault();

      var listItem = $(".item-input").val();
    if (listItem.length > 0) {
		  var itemHtml = "<li><span class='item-check'></span><span class='item-text'>" + listItem + "</span><span class='item-remove'></span></li>";
      $(".shopping-list").append(itemHtml);
      $(".item-input").val("");
      counter++;
      $(".counter").text("Your shopping list has " + counter + " items ");
      // Add the itemHtml section we created for you above to the shopping-list
      // Remove the text the user entered from item-input}
    }
	});
// -------------------


// Step 2
// -------------------
// This code is executed when someone clicks the "X" button
// at the top right of the shopping-item
	$(".shopping-list").on('click', '.item-remove', function(event) {
      // Use event.currentTarget to remove the shopping item from the shopping list
      $(this).parent().remove();
    counter -= 1;
    $(".counter").text("Your shopping list has " + counter + " items ");
  });
// -------------------
  
// Step 3
// This code is executed when someone clicks the checkbox in the shopping-item section
// -------------------
	$(".shopping-list").on('click', '.item-check', function(event) {
      // Use event.currentTarget to add and remove the "complete" class to the checkbox
    if ($(this).hasClass("complete")){$(this).removeClass("complete");}
    else{$(this).addClass("complete");}
    });
  
//counter that tells the user how many items are in your shopping list
  $(".counter").text("Your shopping list has " + counter + " items ");
  
});                      
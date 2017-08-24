using UnityEngine;
using System.Collections;
using UnityEngine.UI;
public class PickUpLight : MonoBehaviour
{

    // Use this for initialization
    private int count;
    public Text countText;
    public Text winText;
    void Start()
    {


        //Initialize count to zero.
        count = 0;

        //Initialze winText to a blank string since we haven't won yet at beginning.
        winText.text = "";

        //Call our SetCountText function which will update the text with the current value for count.
        SetCountText();
    }


    //This function updates the text displaying the number of objects we've collected and displays our victory message if we've collected all of them.
    void SetCountText()
    {
        //Set the text property of our our countText object to "Count: " followed by the number stored in our count variable.
        countText.text = "Count: " + count.ToString();

        //Check if we've collected all 12 pickups. If we have...
        if (count >= 30)
            //... then set the text property of our winText object to "You win!"
            winText.text = "Congrats, you win! You now have enough light to go out and travel the Shadowed Seas - land of eternal darkness.";
    }
    // Update is called once per frame
    void Update()
    {

    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject.CompareTag("Player"))
            Destroy(gameObject);
        count = count + 1;

        //Update the currently displayed count by calling the SetCountText function.
        SetCountText();
    }
}
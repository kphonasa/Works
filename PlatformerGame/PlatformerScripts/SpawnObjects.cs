using UnityEngine;
using System.Collections;
namespace UnityStandardAssets._2D { }
public class SpawnLights : MonoBehaviour
{

    public Transform[] lightSpawns;
    public GameObject light;

    // Use this for initialization
    void Start()
    {

        Spawn();
    }

    void Spawn()
    {
        for (int i = 0; i < lightSpawns.Length; i++)
        {
            int lightFlip = Random.Range(0, 2);
            if (lightFlip > 0)
                Instantiate(light, lightSpawns[i].position, Quaternion.identity);
        }
    }

}

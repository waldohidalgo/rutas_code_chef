using System;
using System.Linq;
public class Test2
{
    public static void LinearSearch()
    {
        // your code goes here
        string input1 = Console.ReadLine();
        string input2 = Console.ReadLine();
        char c = input2[0];

        int n = input1.Length;
        bool isFound = false;
        for (int i = 0; i < n; i++)
        {
            if (input1[i] == c)
            {
                Console.WriteLine(i);
                isFound = true;
                break;
            }
        }
        if (!isFound)
        {
            Console.WriteLine("-1");
        }


    }
}

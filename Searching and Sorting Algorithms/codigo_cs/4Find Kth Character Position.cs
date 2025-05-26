using System;
using System.Linq;

public class Test4
{
    public static void KthCharacter()
    {
        // your code goes here
        string[] input = Console.ReadLine().Split(' ');
        string s1 = input[0];
        char c1 = input[1][0];
        int k = int.Parse(input[2]);

        int count = 0;
        bool isFound = false;
        for (int i = 0; i < s1.Length; i++)
        {
            if (s1[i] == c1)
            {
                count++;
            }
            if (count == k)
            {
                Console.WriteLine(i);
                isFound = true;
                break;
            }
        }
        if (!isFound)
        {
            Console.WriteLine(-1);
        }

    }
}

using System;
using System.Collections.Generic;
public class Test2
{
    public static void SimpleSorting()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        List<int> arr = new List<int>();
        for (int i = 0; i < n; i++)
        {
            arr.Add(int.Parse(Console.ReadLine()));
        }
        arr.Sort();
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine(arr[i]);
        }

    }
}

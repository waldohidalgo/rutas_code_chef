using System;
using System.Linq;

public class Test5
{
    public static void MinandMax()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int max = arr[0];
        int min = arr[0];
        for (int i = 1; i < n; i++)
        {
            if (arr[i] > max)
            {
                max = arr[i];
            }
            if (arr[i] < min)
            {
                min = arr[i];
            }
        }
        Console.WriteLine(min + " " + max);
    }
}
using System;
using System.Linq;


public class Test10
{
    public static void BubbleSort()
    {
        // your code goes here
        int[] arr = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        int n = arr.Length;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (arr[j] < arr[i])
                {
                    (arr[j], arr[i]) = (arr[i], arr[j]);
                }
            }
        }
        Console.WriteLine(string.Join(" ", arr));
    }
}

using System;
using System.Linq;


public class Test9
{
    public static void SortThreeNumbers()
    {
        // your code goes here
        int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
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

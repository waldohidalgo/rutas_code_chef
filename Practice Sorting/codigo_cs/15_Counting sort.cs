using System;
using System.Linq;
using System.Collections.Generic;

public class Test15
{



    static string Aux(int n, int[] arr)
    {
        int min_value = arr.Min();
        int max_value = arr.Max();

        int[] frequency = new int[max_value - min_value + 1];

        for (int i = 0; i < n; i++)
        {
            frequency[arr[i] - min_value]++;
        }
        var sortedArr = new List<(int freq, int val)>();
        for (int i = 0; i < n; i++)
        {
            sortedArr.Add((frequency[arr[i] - min_value], arr[i]));
        }
        sortedArr.Sort();
        return string.Join(" ", sortedArr.Select(t => t.val));

    }
    public static void CountingSort()
    {
        int n = int.Parse(Console.ReadLine());
        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);

        Console.WriteLine(Aux(n, arr));

    }
}

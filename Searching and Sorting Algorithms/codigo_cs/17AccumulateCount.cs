using System;

public class Test17
{
    public static void AccumulateCount()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        int k = int.Parse(Console.ReadLine());
        int[] res = Enumerable.Repeat(0, k).ToArray();

        for (int i = 0; i < n; i++)
        {
            res[arr[i]]++;
        }
        int prev = 0;
        for (int j = 0; j < k; j++)
        {
            res[j] += prev;
            prev = res[j];
        }
        Console.WriteLine(string.Join(" ", res));
    }
}
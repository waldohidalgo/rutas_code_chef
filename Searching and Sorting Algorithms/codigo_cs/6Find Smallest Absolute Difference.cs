using System;

public class Test6
{
    public static void MinAbsDiff()
    {
        // your code goes here
        string input = Console.ReadLine();
        int n = int.Parse(input.Split(' ')[0]);
        int k = int.Parse(input.Split(' ')[1]);
        int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int elem = arr[0];
        for (int i = 1; i < n; i++)
        {
            if (Math.Abs(arr[i] - k) < Math.Abs(elem - k))
            {
                elem = arr[i];
            }
            else if (Math.Abs(arr[i] - k) == Math.Abs(elem - k))
            {
                elem = Math.Min(arr[i], elem);
            }
        }
        Console.WriteLine(elem);
    }
}
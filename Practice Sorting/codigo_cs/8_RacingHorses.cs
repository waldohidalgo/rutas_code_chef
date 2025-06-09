using System;

public class Test8
{
    public static void RacingHorses()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            Array.Sort(arr);
            int min_diff = arr[n - 1] - arr[0];
            for (int j = 1; j < arr.Length; j++)
            {
                if (arr[j] - arr[j - 1] < min_diff)
                {
                    min_diff = arr[j] - arr[j - 1];
                }
            }
            Console.WriteLine(min_diff);
        }
    }
}

using System;
using System.Linq;
public class Test7
{
    public static void FindPairsDivisibleSum()
    {
        // your code goes here
        int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int n = arr[0];
        int k = arr[1];
        for (int t = 0; t < n; t++)
        {
            int[] data = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int p = data[0];
            int q = data[1];
            if ((p + q) % k == 0)
            {
                Console.WriteLine("(" + p + ", " + q + ")");
            }
        }
    }
}

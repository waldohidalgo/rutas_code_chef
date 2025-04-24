using System;
using System.Linq;
public class Test16
{
    public static void RedLight()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            string input = Console.ReadLine();
            int n = int.Parse(input.Split()[0]);
            int k = int.Parse(input.Split()[1]);
            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int count = 0;
            for (int i = 0; i < n; i++)
            {
                if (a[i] > k) count++;
            }
            Console.WriteLine("count" + count);
        }
    }
}

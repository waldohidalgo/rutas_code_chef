using System;
using System.Linq;
public class Test15
{
    public static void Snapchat()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int[] b = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int count = 0;
            int max_streak = 0;
            for (int i = 0; i < n; i++)
            {
                if (a[i] > 0 && b[i] > 0)
                {
                    count++;
                    max_streak = Math.Max(max_streak, count);
                }
                else
                {
                    count = 0;
                }
            }
            Console.WriteLine($"count {max_streak}");
        }
    }
}

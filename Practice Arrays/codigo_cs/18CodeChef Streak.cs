using System;
using System.Linq;
public class Test18
{
    public static void Streak()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int[] b = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int count_a = 0, count_b = 0;
            int max_streak_a = 0, max_streak_b = 0;
            for (int i = 0; i < n; i++)
            {
                if (a[i] > 0)
                {
                    count_a += 1;
                }
                else
                {
                    count_a = 0;
                }
                max_streak_a = Math.Max(max_streak_a, count_a);
                if (b[i] > 0)
                {
                    count_b += 1;
                }
                else
                {
                    count_b = 0;
                }
                max_streak_b = Math.Max(max_streak_b, count_b);

            }

            if (max_streak_a > max_streak_b)
            {
                Console.WriteLine("OM");
            }
            else if (max_streak_a < max_streak_b)
            {
                Console.WriteLine("ADDY");
            }
            else
            {
                Console.WriteLine("DRAW");
            }
        }
    }
}
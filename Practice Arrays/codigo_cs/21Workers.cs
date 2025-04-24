using System;
using System.Linq;
public class Test21
{
    public static void Workers()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        int[] c = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int[] t = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int min_a = (int)Math.Pow(10, 5) + 1;
        int min_t = (int)Math.Pow(10, 5) + 1;
        int min_m = (int)Math.Pow(10, 5) + 1;

        for (int i = 0; i < n; i++)
        {
            if (t[i] == 1)
            {
                min_t = Math.Min(min_t, c[i]);
            }
            else if (t[i] == 2)
            {
                min_a = Math.Min(min_a, c[i]);
            }
            else
            {
                min_m = Math.Min(min_m, c[i]);
            }
        }

        if (min_t + min_a < min_m)
        {
            Console.WriteLine(min_t + min_a);
        }
        else
        {
            Console.WriteLine(min_m);
        }
    }
}

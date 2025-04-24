using System;
using System.Linq;
public class Test14
{
    public static void TheSquidGame()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int total_sum = 0;
            int min_val = (int)Math.Pow(10, 4) + 1;
            for (int i = 0; i < n; i++)
            {

                total_sum += a[i];
                if (a[i] < min_val) min_val = a[i];
            }
            Console.WriteLine(total_sum - min_val);


        }
    }
}

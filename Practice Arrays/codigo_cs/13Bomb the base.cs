using System;
using System.Linq;

public class Test13
{
    public static void BombTheBase()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            string input = Console.ReadLine();
            int n = int.Parse(input.Split()[0]);
            int x = int.Parse(input.Split()[1]);
            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            for (int i = n - 1; i >= 0; i--)
            {
                if (a[i] < x)
                {
                    Console.WriteLine(i + 1);
                    break;
                }
            }
            Console.WriteLine(0);

        }

    }
}

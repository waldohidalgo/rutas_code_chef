using System;
using System.Linq;
public class Test4
{
    public static void WATestCases()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] s = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            string v = Console.ReadLine();
            int minVal = 101;

            for (int j = 0; j < n; j++)
            {
                if (v[j] == '0' && s[j] < minVal)
                {
                    minVal = s[j];
                }
            }
            Console.WriteLine(minVal);

        }
    }
}

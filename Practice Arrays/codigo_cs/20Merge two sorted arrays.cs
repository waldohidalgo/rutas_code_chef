using System;
using System.Linq;
public class Test20
{
    public static void MergeSort()
    {
        // your code goes here
        string input = Console.ReadLine();
        int n = int.Parse(input.Split()[0]);
        int m = int.Parse(input.Split()[1]);
        int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int[] b = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int[] res = new int[n + m];
        int i = 0, j = 0, k = 0;

        while (i < n && j < m)
        {
            if (a[i] <= b[j])
            {
                res[k++] = a[i++];
            }
            else
            {
                res[k++] = b[j++];
            }
        }

        while (i < n)
        {
            res[k++] = a[i++];
        }

        while (j < m)
        {
            res[k++] = b[j++];
        }

        Console.WriteLine(string.Join(" ", res));

    }
}

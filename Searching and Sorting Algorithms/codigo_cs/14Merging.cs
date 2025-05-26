using System;
using System.Linq;
public class Test14
{
    public static void Merge()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        int[] a = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        int m = int.Parse(Console.ReadLine());
        int[] b = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        int[] c = new int[n + m];
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < n && j < m)
        {
            if (a[i] < b[j])
            {
                c[k] = a[i];
                i++;
            }
            else
            {
                c[k] = b[j];
                j++;
            }
            k++;
        }
        while (i < n)
        {
            c[k] = a[i];
            i++;
            k++;
        }
        while (j < m)
        {
            c[k] = b[j];
            j++;
            k++;
        }
        Console.WriteLine(string.Join(" ", c));
    }

}

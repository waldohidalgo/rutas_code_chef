using System;

public class Test5
{
    public static void Facebook()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] a = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            int[] b = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            // your code goes here
            int maxComments = 0;
            int maxVal = 0;
            int position = 0;
            for (int index = 0; index < n; index++)
            {
                if (a[index] > maxVal)
                {
                    maxVal = a[index];
                    maxComments = b[index];
                    position = index + 1;
                }
                else if (a[index] == maxVal)
                {
                    if (b[index] > b[position - 1])
                    {
                        maxComments = b[index];
                        position = index + 1;
                    }
                }
            }
            Console.WriteLine(position);
        }
    }
}
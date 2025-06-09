using System;

public class Test7
{
    public static void SimpleStatistics()
    {
        // your code goes here

        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {

            string input = Console.ReadLine();
            int n = int.Parse(input.Split(' ')[0]);
            int k = int.Parse(input.Split(' ')[1]);
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            // your code goes here
            Array.Sort(arr);
            int sum = 0;
            for (int j = k; j < n - k; j++)
            {
                sum += arr[j];
            }
            double average = (double)sum / (n - 2 * k);
            Console.WriteLine(average.ToString("F6"));

        }
    }
}

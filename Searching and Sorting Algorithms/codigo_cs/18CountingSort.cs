using System;

public class Test18
{
    public static void CountingSort(int[] arr)
    {
        int minVal = arr.Min();
        int maxVal = arr.Max();
        int width = maxVal - minVal + 1;
        int[] count = new int[width];
        foreach (int el in arr)
        {
            int index = el - minVal;
            count[index] += 1;
        }
        for (int i = 1; i < width; i++)
        {
            count[i] += count[i - 1];
        }
        int n = arr.Length;
        int[] res = new int[n];
        for (int i = n - 1; i >= 0; i--)
        {
            int num = arr[i];
            int index = num - minVal;
            count[index] -= 1;
            res[count[index]] = num;
        }

        // for (int i = 0; i < n; i++)
        // {
        //     arr[i] = res[i];
        // }
        Console.WriteLine(string.Join(" ", res));





    }
}
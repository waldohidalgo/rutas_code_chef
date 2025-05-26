
using System;


public class Test19
{

    public static void RadixSort(int[] arr)
    {
        int n = arr.Length;
        int maxVal = arr[0];

        for (int i = 1; i < n; i++)
        {
            if (arr[i] > maxVal)
            {
                maxVal = arr[i];
            }
        }
        int exp = 1;
        while (maxVal / exp > 0)
        {
            CountingSort(arr, exp);
            exp *= 10;
        }
    }

    static void CountingSort(int[] arr, int exp)
    {

        int n = arr.Length;
        int[] count = new int[10];
        int[] output = new int[n];
        for (int i = 0; i < n; i++)
        {
            count[(arr[i] / exp) % 10]++;
        }
        for (int i = 1; i < 10; i++)
        {
            count[i] += count[i - 1];
        }
        for (int i = n - 1; i >= 0; i--)
        {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }
        for (int i = 0; i < n; i++)
        {
            arr[i] = output[i];
        }
    }

}
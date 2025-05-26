using System;
using System.Linq;

public class Test15

{

    static void Merge(int[] arr, int l, int m, int r)
    {
        int i, j;
        int[] left = new int[m - l + 1];
        int[] right = new int[r - m];
        for (i = 0; i < left.Length; i++)
            left[i] = arr[l + i];
        for (j = 0; j < right.Length; j++)
            right[j] = arr[m + 1 + j];
        int k = l;
        i = j = 0;
        while (i < left.Length && j < right.Length)
        {
            if (left[i] <= right[j])
                arr[k++] = left[i++];
            else
                arr[k++] = right[j++];
        }
        while (i < left.Length)
            arr[k++] = left[i++];
        while (j < right.Length)
            arr[k++] = right[j++];


    }

    public static void MergeSort(int[] arr, int l, int r)
    {
        if (l == r)
            return;
        int mid = (l + r) / 2;
        MergeSort(arr, l, mid);
        MergeSort(arr, mid + 1, r);
        Merge(arr, l, mid, r);

    }
}
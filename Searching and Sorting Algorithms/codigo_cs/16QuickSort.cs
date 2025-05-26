using System;


public class Test16

{

    public static void QuickSort(int[] arr, int low, int high)
    {
        // write your code here
        if (low >= high)
        {
            return;
        }
        int pivot = Partition(arr, low, high);
        QuickSort(arr, low, pivot - 1);
        QuickSort(arr, pivot + 1, high);
    }

    static int Partition(int[] arr, int low, int high)
    {
        // write your code here
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        i++;
        int temp2 = arr[i];
        arr[i] = pivot;
        arr[high] = temp2;
        return i;

    }

}
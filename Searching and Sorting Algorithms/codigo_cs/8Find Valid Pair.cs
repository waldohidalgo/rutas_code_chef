using System;

public class Test8
{
    public static void GetValidPairs()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        var arr = new Tuple<int, int>[n];
        for (int i = 0; i < n; i++)
        {
            string[] parts = Console.ReadLine().Split();
            int p = int.Parse(parts[0]);
            int q = int.Parse(parts[1]);
            arr[i] = Tuple.Create(p, q);
        }
        string[] lr = Console.ReadLine().Split();
        int l = int.Parse(lr[0]);
        int r = int.Parse(lr[1]);
        for (int i = 0; i < n; i++)
        {
            int sum = arr[i].Item1 + arr[i].Item2;
            int product = arr[i].Item1 * arr[i].Item2;
            if (l <= sum && sum <= r && l <= product && product <= r)
            {
                Console.WriteLine(arr[i].Item1 + " " + arr[i].Item2);
            }
        }
    }
}

public class BucketSort {

    public static void main(String[] args) {

        float[] arr = {0.41f, 0.21f, 0.87f, 0.55f, 0.39f,
                       0.06f, 0.77f, 0.48f, 0.32f};

        bucketSort(arr);

        System.out.println("Sorted Array:");

        for (float num : arr) {
            System.out.print(num + " ");
        }
    }

    public static void insertionSort(float[] arr, int n) {

        for (int i = 1; i < n; i++) {

            float key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }

    public static void bucketSort(float[] arr) {

        if (arr.length == 0) {
            return;
        }

        int n = arr.length;

        float[][] buckets = new float[n][n];

        int[] bucketSize = new int[n];

        for (int i = 0; i < n; i++) {

            int index = (int) (n * arr[i]);

            buckets[index][bucketSize[index]] = arr[i];

            bucketSize[index]++;
        }

        // Sort each bucket
        for (int i = 0; i < n; i++) {
            insertionSort(buckets[i], bucketSize[i]);
        }

        // Combine buckets
        int pos = 0;

        for (int i = 0; i < n; i++) {

            for (int j = 0; j < bucketSize[i]; j++) {

                arr[pos++] = buckets[i][j];
            }
        }
    }
}

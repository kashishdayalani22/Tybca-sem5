public class MergeSort{
    public static void main(String[] args) {
        int[] data1 = {38, 27, 43, 3, 9, 82, 10};

        mergeSort(data1, 0, data1.length - 1);

        printArray(data1);
    }

    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);            // dividing array and applying merge sort on left half
            mergeSort(arr, mid + 1, right);       // dividing array and applying merge sort on right half

            //Combining the array
            merge(arr, left, mid, right);
        }
    }

    public static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;        //determining the size of L (left) array | +1 for converting index to length 
                                        // value of left won't be 0 each time so we can't take mid as size directly
        int n2 = right - mid;           //determining the size of R (right) array

        //temporary arrays, not final output
        int[] L = new int[n1];        
        int[] R = new int[n2];

        // adding values in L
        for (int i = 0; i < n1; ++i) {
            L[i] = arr[left + i];
        }
        // Adding values in R
        for (int j = 0; j < n2; ++j) {
            R[j] = arr[mid + 1 + j];
        }

        // these values will be used for indexing
        // i is for L array
        // j is for R array
        // k = left taki wo har recursive call pe wo lowest value le jo humne function mai pass ki hai
        // last mai k bhi 0 hoga, jab ye final output ke liye call hoga, yani line 5 wala
        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {
            //dono array ke elements compare karte hai
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                // jis array mai se element dala arr mai sirf uski indexing increment karenge
                // bolna upar wala, niche wala tere liye hai
                // agar L array ka element bada hai to uska next element compare karenge isliye sirf i++
                i++;                
            } else {
                //else case matlab array R ka element bada hai, toh usko add karenge
                arr[k] = R[j];
                j++;
            }
            //k ki value increse hogi hee kyuki wo dono array mai se kisi ek ka toh element lega hee
            k++;
        }

        // ab agar L array mai elements baki hai to unko directlyo add kar denge
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        // same, agar R array mai elements baki hai to unko directly add kar denge
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
    // array print karne ke liye function
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}

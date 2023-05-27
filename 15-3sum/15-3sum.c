/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void merge(int arr[], int l, int m, int r){
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for(i = 0; i < n1; i++){
        L[i] = arr[l + i];
    }
    for(j = 0; j < n2; j++){
        R[j] = arr[m + 1 + j];
    }
    i = 0;
    j = 0;
    k = l;
    while(i < n1 && j < n2){
        if(L[i] <= R[j]){
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while(i < n1){
        arr[k] = L[i];
        i++;
        k++;
    }
    while(j < n2){
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r){
    if (l < r){
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int** res = (int**)malloc(sizeof(int*)*8);
    *returnColumnSizes = (int**)malloc(sizeof(int)*8);
    int resSize = 0;
    int bSize = 8;
    mergeSort(nums, 0, numsSize - 1);
    for(int i = 0; i < numsSize; i++){
        if(i > 0 && nums[i] == nums[i - 1]){
            continue;
        }
        int l = i + 1;
        int r = numsSize - 1;
        while(l < r){
            int threeSum = nums[i] + nums[l] + nums[r];
            if(threeSum > 0){
                r --;
            } else if (threeSum < 0){
                l++;
            } else {
                res[resSize] = (int*)malloc(sizeof(int)*3);
                (*returnColumnSizes)[resSize] = 3;
                res[resSize][0] = nums[i];
                res[resSize][1] = nums[l];
                res[resSize][2] = nums[r];
                resSize++;
                if(resSize == bSize){
                    bSize *= 2;
                    res = (int**)realloc(res, sizeof(int*)*bSize);
                    (*returnColumnSizes) = (int**)realloc((*returnColumnSizes), sizeof(int)*bSize);
                }
                l++;
                while(nums[l] == nums[l - 1] && l < r){
                    l++;
                }
            }
        }
    }
    *returnSize = resSize;
    return res;
}
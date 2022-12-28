#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char buff[100] = {};
int array[10][10];

int getArrSize(char *buff){
    int num = 0;
    for(num = 0; num < sizeof(buff); num++){
        if(buff[num] == NULL) {
            break;
        }        
    }
    return num + 1;
}
void putArray(char *array){
    array[0] = ' ';
    for (int i = 1; i < sizeof(buff); i++)
    {
        if (buff[i] == NULL)
        {
            break;
        }
        else{
            array[i] = buff[i - 1];
            array[i+1] = buff[i];
        }
    }
}

int getMin(int a, int b, int c){
    int min = a;
    if (min > b)min = b;
    if (min > c) min = c; 
    return min;
}
int getMin2(int a, int b){
    int min = a;
    if (min > b) min = b; 
    return min;
}
int cmp(int replace, int minAdd){
    if(replace < minAdd) return replace;
    else return minAdd;
}
void getDistance(char *a, char *b){
    int testa = 0;
    for (int i = 0; i < sizeof(a); i++)
    {
        array[i][0] = i * 5;
    }
    for (int j = 0; j < sizeof(b); j++)
    {
        array[0][j] = j * 5;
    }
    for (int i = 1; i < sizeof(a); i++)
    {
        for (int j = 1; j < sizeof(b); j++)
        {
            int minAdd = getMin2(array[i - 1][j], array[i][j - 1]) + 5;
            int result = 0;

            if ((int)a[i] == (int)b[j]){// 값이 같을때
                result = array[i - 1][j - 1];
                array[i][j] = cmp(result,minAdd);
            }
            else if (!(0x39 >= (int)b[j] && (int)b[j] >= 0x30) && !(0x39>(int)a[i] && (int)a[i] >0x31) && (abs((int)a[i] - (int)b[j]) == 32)){ //교체 중  대소문자 차이
                result = array[i - 1][ j - 1] + 1;
                array[i][j] = cmp(result,minAdd);
            }
            else if ((0x39 >= (int)b[j] && (int)b[j] >= 0x30) && (0x39>(int)a[i] && (int)a[i] >= 0x30)){ //둘 다 숫자인 경우
                int pd = abs((int)a[i] - (int)b[j]);
                result = array[i - 1][ j - 1] + pd;
                printf("%d",result);
                array[i][j] = cmp(result,minAdd);
            } 
            else if ((!(0x39 >= (int)b[j] && (int)b[j] >= 0x30) && (0x39>(int)a[i] && (int)a[i] >= 0x30)) || ((0x39 >= (int)b[j] && (int)b[j] >= 0x30) && !(0x39>(int)a[i] && (int)a[i] >= 0x30))){ //교체 중 알파벳 숫자 차이
                result = array[i - 1][ j - 1] + 7;
                array[i][j] = cmp(result,minAdd);   
            }
            //삽입 삭제 교체 중 둘 다 알파벳이면서 다른 경우
            else array[i][j] = minAdd;
        }
    }
}

int main(){
    printf("-입력\n");
    scanf("%s",buff);
    char a[getArrSize(buff)];
    putArray(a);
    scanf("%s",buff);
    char b[getArrSize(buff)];
    putArray(b);
    
    getDistance(a,b);
    printf("최소 거리 : %d\n",array[sizeof(a) - 1][sizeof(b) - 1]);

    return 0;
}
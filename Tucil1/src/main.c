#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "boolean.h"

int main(int argc, char const *argv[])
{
// KAMUS
    typedef char ElType;
    
    typedef struct { // Matrix untuk menyimpan puzzle
    ElType contents[100][100];
    int rowEff; /* banyaknya ukuran baris yg terdefinisi */
    int colEff; /* banyaknya ukuran kolom yg terdefinisi */
    } Matrix;
    /* rowEff >= 1 dan colEff >= 1 */
    /* Indeks matriks yang digunakan: [0..99][0..99] */
    /* Memori matriks yang dipakai selalu di "ujung kiri atas" */

    typedef struct { // list untuk menyimpan kata yang dicari
        ElType contents[50];
        int row[50]; // indeks baris dari karakter yang dicari
        int col[50]; // indeks kolom dari karakter yang dicari
        int idxEff; // indeks effektif yang digunakan >= 1
    } Kata;

    char cc , file_name[25];
    Matrix m;
    Kata word;
    FILE *fp;
    double totalTime; // Variable untuk menyimpan total waktu yang dibutuhkan untuk eksekusi program
    struct timespec begin, end; // Waktu awal dan akhir eksekusi 
    long int totalComparison = 0; // Total jumlah perbandingan huruf


// ALGORITMA
    // Membaca input text
    printf("Masukkan nama file input: ");
    scanf("%s",file_name);
    fp = fopen(file_name, "r");

    // Mengecek file ada atau tidak
    if (fp == NULL) {
        perror("");
        exit(EXIT_FAILURE);
    } else {
        boolean flagPrec = false, flagAfter = false; // Penanda baris kosong
        int i = 0, j = 0; // index baris dan kolom matriks
        // Membaca Matriks huruf puzzle
        cc = fgetc(fp);
        while(!flagAfter) {
            if (cc != '\n') {
                flagPrec = false;
                if (cc != ' ') {
                    m.contents[i][j] = cc;
                    j++;
                }
            } else {
                if (!flagPrec) {
                    m.colEff = j + 1;
                    flagPrec = true;
                    j = 0;
                    i++;
                } else {
                    flagAfter = true;
                }
            }
            cc = fgetc(fp);
        }

        m.rowEff = i;

        // Membaca daftar kata yang dicari di dalam puzzle dan menampilkan
        // di mana kata tersebut berada di dalam puzzle 
        i = 0;

        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &begin);
        boolean flag = false;
        while (!flag) {
            if (cc != '\n' && cc != EOF) {
                if (cc != ' ') {
                    word.contents[i] = cc;
                    i++;
                }
            } else {
                if (cc == EOF) {
                    flag = true;
                }
                word.idxEff = i;
                i = 0;

                // Menghitung waktu yang dibutuhkan untuk eksekusi program
                // begin = clock(); // waktu mulai

                if (word.idxEff != 0) { // Mengecek apakah string kosong
                    // Mencari kata dalam puzzle
                    int row = 0, col = 0, idx;
                    boolean found = false;
                    while (!found && row != m.rowEff && col != m.colEff) {
                        // printf("%d ",row);
                        idx = 0;
                        totalComparison++;
                        if (m.contents[row][col] == word.contents[idx]) {
                            // Mengecek vertikal ke atas
                            if (row + 1 - word.idxEff >= 0) {
                                int k = row;
                                while (idx < word.idxEff && m.contents[k][col] == word.contents[idx]) {
                                    totalComparison++;
                                    word.row[idx] = k;
                                    word.col[idx] = col;
                                    k--;
                                    idx++;
                                }
                                if (idx == word.idxEff) {
                                    found = true;
                                } else {
                                    totalComparison++;
                                    idx = 0;
                                } 
                            } 
                            // Mengecek Vertikal ke bawah
                            if (!found && row + word.idxEff <= m.rowEff) { 
                                int k = row;
                                while (idx < word.idxEff && m.contents[k][col] == word.contents[idx]) {
                                    totalComparison++;
                                    word.row[idx] = k;
                                    word.col[idx] = col;
                                    k++;
                                    idx++;
                                }
                                if (idx == word.idxEff) {
                                    found = true;
                                } else {
                                    totalComparison++;
                                    idx = 0;
                                }
                            }
                            // Mengecek horizontal ke kanan
                            if (!found && col + word.idxEff <= m.colEff) {
                                int k = col;
                                while (idx < word.idxEff && m.contents[row][k] == word.contents[idx]) {
                                    totalComparison++;
                                    word.row[idx] = row;
                                    word.col[idx] = k;
                                    k++;
                                    idx++;
                                }
                                if (idx == word.idxEff) {
                                    found = true;
                                } else {
                                    totalComparison++;
                                    idx = 0;
                                }
                            }
                            // Mengecek horizontal ke kiri
                            if (!found && col + 1 - word.idxEff >= 0) {
                                int k = col;
                                while (idx < word.idxEff && m.contents[row][k] == word.contents[idx]) {
                                    totalComparison++;
                                    word.row[idx] = row;
                                    word.col[idx] = k;
                                    k--;
                                    idx++;
                                }
                                if (idx == word.idxEff) {
                                    found = true;
                                } else {
                                    totalComparison++;
                                    idx = 0;
                                }
                            }
                            // Mengecek diagonal ke kanan atas
                            if (!found && (col + word.idxEff <= m.colEff) && (row + 1 - word.idxEff >= 0)) {
                                int p = row, q = col;
                                while (idx < word.idxEff && m.contents[p][q] == word.contents[idx]) {
                                    totalComparison++;
                                    word.row[idx] = p;
                                    word.col[idx] = q;
                                    p--;
                                    q++;
                                    idx++;
                                }
                                if (idx == word.idxEff) {
                                    found = true;
                                } else {
                                    totalComparison++;
                                    idx = 0;
                                }
                            }
                            // Mengecek diagonal ke kanan bawah
                            if (!found && (col + word.idxEff <= m.colEff) && (row + word.idxEff <= m.rowEff)) {
                                int p = row, q = col;
                                while (idx < word.idxEff && m.contents[p][q] == word.contents[idx]) {
                                    totalComparison++;
                                    word.row[idx] = p;
                                    word.col[idx] = q;
                                    p++;
                                    q++;
                                    idx++;
                                }
                                if (idx == word.idxEff) {
                                    found = true;
                                } else {
                                    totalComparison++;
                                    idx = 0;
                                }
                            }
                            // Mengecek diagonal ke kiri atas
                            if (!found && (col + 1 - word.idxEff >= 0) && (row + 1 - word.idxEff >= 0)) {
                                int p = row, q = col;
                                while (idx < word.idxEff && m.contents[p][q] == word.contents[idx]) {
                                    totalComparison++;
                                    word.row[idx] = p;
                                    word.col[idx] = q;
                                    p--;
                                    q--;
                                    idx++;
                                }
                                if (idx == word.idxEff) {
                                    found = true;
                                } else {
                                    totalComparison++;
                                    idx = 0;
                                }
                            }
                            // Mengecek diagonal ke kiri bawah
                            if (!found && (col + 1 - word.idxEff >= 0) && (row + word.idxEff <= m.rowEff)) {
                                int p = row, q = col;
                                while (idx < word.idxEff && m.contents[p][q] == word.contents[idx]) {
                                    totalComparison++;
                                    word.row[idx] = p;
                                    word.col[idx] = q;
                                    p++;
                                    q--;
                                    idx++;
                                }
                                if (idx == word.idxEff) {
                                    found = true;
                                } else {
                                    totalComparison++;
                                    idx = 0;
                                }
                            }
                        } 

                        if (!found) {
                            if (col == m.colEff-1) {
                                col = 0;
                                row++;
                            } else {
                                col++;
                            }
                        }
                    }
                    
                    // end = clock(); // waktu akhir

                    // Output ke layar
                    if (found) {
                        int r;
                        for (int p = 0; p < m.rowEff; p++) {
                            for (int q = 0; q < m.colEff; q++) {
                                found = false; r = 0;
                                while (!found && r < word.idxEff) {
                                    if (p == word.row[r] && q == word.col[r]) {
                                        found = true;
                                    } else {
                                        r++;
                                    }
                                }
                                if (found) {
                                    if (q != m.colEff - 1) {
                                        printf("%c ", m.contents[p][q]);
                                    } else {
                                        printf("%c\n", m.contents[p][q]);
                                    }
                                    r++;
                                } else {
                                    if (q != m.colEff - 1) {
                                        printf("- ");
                                    } else {
                                        printf("\n");
                                    }
                                }
                            }
                        }
                        printf("\n");
                    }

                    // totalTime += (end - begin) / CLOCKS_PER_SEC;
                }
            }
            cc = fgetc(fp);
        }
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end);
        totalTime = (end.tv_sec - begin.tv_sec) + (end.tv_nsec - begin.tv_nsec) / 1e9;
    }    

    fclose(fp);    

    // Output total waktu eksekusi program
    printf("Waktu eksekusi program: %.10lf seconds.\n", totalTime);
    printf("Total perbandingan huruf: %d.\n", totalComparison);

    return 0;
}
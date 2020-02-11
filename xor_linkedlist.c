#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

/**
 * XOR Linked list.
 * Warning: contains a lot of pointer arithmetic. Seg faults expected.
 */
typedef struct XORList{
    struct XORList *both;
    int data;
} XORList;

XORList *newList (int startVal) {
    XORList *lst = malloc(sizeof(XORList));
    printf("allocating %p\n", lst);
    lst->both = NULL;
    lst->data = startVal;
    return lst;
}

XORList* getNextPtr(void *both, void *prev) {
    return (XORList *) ((uintptr_t) both ^ (uintptr_t) prev);
}

void printList(XORList *lst) {
    XORList *itr = lst;
    XORList *next = lst->both;
    XORList *previous = NULL;
    while (next != NULL) {
        printf("[%p, %d] -> ", itr, itr->data);
        previous = itr;
        itr = next;
        next = getNextPtr(itr->both, previous);
    }
    printf("[%p, %d]", itr, itr->data);
    printf("\n");
}

void addElement(XORList *lst, int data) {
    XORList *itr = lst;
    XORList *next = lst->both;
    XORList *previous = NULL;
    while (next != NULL) {
        previous = itr;
        itr = next;
        next = getNextPtr(itr->both, previous);
    }
    XORList *newNode = newList(data);
    newNode->both = itr;
    itr->both = (XORList *) ((uintptr_t)newNode ^ (uintptr_t)previous);
}

int getElement(XORList *lst, int index) {
    int count = 0;
    XORList *itr = lst;
    XORList *next = lst->both;
    XORList *prev = NULL;
    while (count < index) {
        if (next == NULL) {
            printf("ERROR, tried to get index out of bounds. Aborting.\n");
            return -1;
        }
        prev = itr;
        itr = next;
        next = getNextPtr(itr->both, prev);
        count++;
    }
    return itr->data;
}

/**
 * Helper function for deleting a list.
 */
void freeNode(XORList *node, XORList *previous) {
    if (getNextPtr(node->both, previous) != NULL) { // not at the end
        freeNode(getNextPtr(node->both, previous), node); // free the next node first
    }
    printf("freeing pointer %p\n", node);
    free(node); // then free yourself
}
void deleteList(XORList *lst) {
    freeNode(lst, NULL);
}

int main() {
    XORList *myList = (XORList *)newList(1);
    addElement(myList, 2);
    addElement(myList, 3);
    addElement(myList, 4);
    addElement(myList, 5);
    addElement(myList, 6);
    /* printf("%d\n", getElement(myList, 0)); */
    /* printf("%d\n", getElement(myList, 5)); */
    /* printf("%d\n", getElement(myList, 3)); */
    printList(myList);
    deleteList(myList);
}

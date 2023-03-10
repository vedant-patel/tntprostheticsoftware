#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node* left;
    struct node* right;
};

void preorderTraversal(struct node* root) {
    if (root == NULL) return;
    printf("%d ->", root->value);
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}

struct node* createNode(int value) {
    struct node* newNode = malloc(sizeof(struct node));
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;

    return newNode;
}

// Insert on the left of the node
struct node* insertLeft(struct node* root, int value) {
    root->left = createNode(value);
    return root->left;
}

// Insert on the right of the node
struct node* insertRight(struct node* root, int value) {
    root->right = createNode(value);
    return root->right;
}


int main() {
    struct node Node1;
    Node1.left = createNode(0);
    Node1.right = createNode(23);
    printf("\nPreorder traversal \n");           
    preorderTraversal(*Node1);

}
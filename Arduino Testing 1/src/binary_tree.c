#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct node {
    int value;
    struct node* left;
    struct node* right;
};

// Create a new Node
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
 

}



void loop() {
    int left_bit = 1, right_bit = 1, middle_bit = 1;

    // Creates root node
    struct node* root = createNode(middle_bit);

    // Creates first layer
    struct node* l_child = insertLeft(root, left_bit);
    struct node* r_child = insertRight(root, right_bit);

    // Creates second left layer subtree
    struct node* thumb  = insertLeft(l_child, 1);
    struct node* lr_child = insertRight(l_child, right_bit);

    // Creates second right layer subtree
    struct node* rl_child = insertLeft(r_child, right_bit);
    struct node* rr_child = insertRight(r_child, right_bit);

    // Creates third right layer subtree in left subtree
    struct node* ring_fin = insertLeft(lr_child, 4);
    struct node* pinky = insertRight(lr_child, 5);

    // Creates third left layer subtree in right subtree
    struct node* index_fin = insertLeft(rl_child, 2);
    struct node* middle_fin = insertRight(rl_child, 3);

    // Creates third right layer subtree in right subtree
    struct node* wrist_up = insertLeft(rr_child, 6);
    struct node* wrist_down = insertRight(rr_child, 7);

    //creating empty nodes 
    struct node* empty1  = insertRight(wrist_down, -1);

/* Looping code*/
int final_value = 0; 
int layer_num = 0;
while (root->right->value != -1){ //add the LEFT NODE STATEMENT TOO
    if (root->value == 0) {
        printf("%d", root->value);
        root = root->left; 
        }
    else {
        final_value += pow(2, layer_num);
        printf("%d",root->value);
        root = root->right;
    }
    layer_num += 1;
}
printf("%d", final_value);
}




//printf("%d", wrist_down->right->value);
//root->value = root->left->value;
//printf("%d", root->value);

// Inorder traversal
// void inorderTraversal(struct node* root) {
//     if (root == NULL) return;
//     inorderTraversal(root->left);
//     printf("%d ->", root->value);
//     inorderTraversal(root->right);
// }

// Preorder traversal
/*void preorderTraversal(struct node* root) {
    if (root == NULL) return;
    printf("%d ->", root->value);
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}*/

// Postorder traversal
// void postorderTraversal(struct node* root) {
//     if (root == NULL) return;
//     postorderTraversal(root->left);
//     postorderTraversal(root->right);
//     printf("%d ->", root->value);
// }

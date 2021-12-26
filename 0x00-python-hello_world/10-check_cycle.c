#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it
 *@list: pointer to the linked list
 *Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
listint_t *l1 = list;
listint_t *l2 = list;
while (l1 && l2 && l2->next)
{
l1 = l1->next;
l2 = l2->next->next;
if (l1 == l2)
return (1);
}
return (0);
}

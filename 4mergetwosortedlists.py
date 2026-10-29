class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# LISTA 1: 1 -> 2 -> 4
lista1 = ListNode(1)
lista1.next = ListNode(2)
lista1.next.next = ListNode(4)

# LISTA 2: 1 -> 3 -> 4
lista2 = ListNode(1)
lista2.next = ListNode(3)
lista2.next.next = ListNode(4)

def imprimir_lista(nodo):
    elementos = []
    while nodo:
        elementos.append(str(nodo.val))
        nodo = nodo.next
    print(" -> ".join(elementos) + " -> None")

def mergeTwoLists(self, lista1, lista2):
    dummy = ListNode()
    current = dummy

    while lista1 and lista2:
        if lista1.val <= lista2.val:
            current.next = lista1
            lista1 = lista1.next
        else:
            current.next = lista2
            lista2 = lista2.next
        
        current = current.next
    current.next = lista1 if lista1 else lista2
    return dummy.next

resultado = mergeTwoLists(None, lista1, lista2)
imprimir_lista(resultado)
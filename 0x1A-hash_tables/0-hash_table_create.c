#include "hash_tables.h"

/**
 * hash_table_create - Create a hash table
 *
 * @size: The size of the array
 *
 * Return: returns pointer to the newly created hash table
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *hash_table;
	unsigned long int i;

	/* allocate table */

	hash_table = malloc(sizeof(hash_table_t));

	if (hash_table == NULL)
		return (NULL);
	hash_table->size = size;

	/* allocate table array */

	hash_table->array = malloc(sizeof(hash_node_t) * size);
	if (hash_table->array == NULL)
	{
		free(hash_table);
		return (NULL);
	}

	/* set each index of the table to null */

	i = 0;
	for (; i < size; i++)
	{
		hash_table->array[i] = NULL;
	}

	return (hash_table);
}

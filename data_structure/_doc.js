/**
 * 1.
 * @name    HashMap (dict, set, defaultdict, Hash Table)
 *          Prefer to use Hash Table - faster, sync, allows null values.
 *
 * Complexity:
 *  @time       Insert - O(1)
 *              Search - O(1)
 *              Delete - O(1)
 *
 *
 * Advantages:
 *  1) Constant time for three main operations.
 *
 */

/**
 * 2.
 * @name    Self-balancing BST (no default implementation)
 *
 * Complexity:
 *  @time       Insert - O(1)
 *              Search - O(1)
 *              Delete - O(1)
 *
 *
 * Advantages:
 *  1) In-order traversing gives you sorted values.
 *  2) From the above - suitable for range queries and for finding closest lower and greater values.
 *  3) Easy to implement by yourself.
 *  4) Guaranteed time complexity in all cases.
 */
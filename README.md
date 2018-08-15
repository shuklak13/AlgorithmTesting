To test a sorting function, replace the `sort` function in `test_sort.py` with your own. Then, run `test_sort.py`.

For instance, if you wanted to test the provided `selection_sort` function, you would replace the following two lines at the start of `test_sort.py`

    import examples.insertion_sort
    sort = examples.insertion_sort.insertion_sort

with the following

    import examples.selection_sort
    sort = examples.selection_sort.selection_sort
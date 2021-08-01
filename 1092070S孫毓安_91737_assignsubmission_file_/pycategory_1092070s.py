class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        """please key in the categories for further classification.
        """
        # 1. Initialize self._categories as a nested list.
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]

    def view(self, categories=[], prefix=()):
        """show you the categories structure.
        """
        # 1. Define the formal parameters so that this method
        #    can be called recursively.
        # 2. Recursively print the categories with indentation.
        # 3. Alternatively, define an inner function to do the recursion.
        if categories == []:
            categories = self._categories
        if type(categories) == list:
            index = 0
            for i in categories:
                if type(i) == str:
                    index += 1
                self.view(i, prefix+(index,))
        else:
            print(' '*2*(len(prefix)-1) + '- ' + categories)

    def is_category_valid(self, category, categories=[]):
        """check whether the category of the item you would like to add exists in categories list.
        """
        # 1. Define the formal parameters so that a category name can be
        #    passed in and the method can be called recursively.
        # 2. Recursively check if the category name is in self._categories.
        # 3. Alternatively, define an inner function to do the recursion.
        if categories == []:
            categories = self._categories
        if type(categories) == list:
            for i in categories:
                if self.is_category_valid(category, i) == "yes":
                    return "yes"
            return "no" 
        else:
            if category == categories:
                return "yes"

    def find_subcategories(self, category):
        # def find_subcategories_gen(category, categories):
        #     if type(categories) == list: # recursive case
        #         for child in categories:
        #             yield from find_subcategories_gen(category, child)
        #     else: # base case
        #         yield categories

        # def find_subcategories_gen(category, categories):
        #     if type(categories) == list: # recursive case
        #         for child in categories:
        #             yield from find_subcategories_gen(category, child)
        #     else: # base case
        #         if categories == category:
        #             yield categories

        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index + 1], True)
            else:
                if categories == category or found==True:
                    yield categories

        return [i for i in find_subcategories_gen(category, self._categories)]
        # A list generated by find_subcategories_gen(category, self._categories)

    def getCategories(self):
        return self._categories
    # def find_subcategories(self, category, categories=[]):
    #     """ takes a category name to find and the predefined list categories as parameters, 
    #     and returns a non-nested list containing the specified category and all the subcategories under it.
    #     """
    #     # 1. Define the formal parameters so that a category name can be
    #     #    passed in and the method can be called recursively.
    #     # 2. Recursively find the target category and call the
    #     #    self._flatten method to get the subcategories into a flat list.
    #     # 3. Alternatively, define an inner function to do the recursion.
    #     if categories == []:
    #         categories = self._categories
    #     if type(categories) == list:
    #         for v in categories:
    #             p = self.find_subcategories(category, v)
    #             if p == True:
    #                 index = categories.index(v)
    #                 if index + 1 < len(categories) and \
    #                         type(categories[index + 1]) == list:
    #                     return self._flatten(categories[index:index + 2])
    #                 else:
    #                     # return only itself if no subcategories
    #                     return [v]
    #             if p != []:
    #                 return p
    #     return True if categories == category else []

    # def _flatten(self, L):
    #     """ return a flat list that contains all element in the nested list L.
    #     for example, flatten([1, 2, [3, [4], 5]]) returns [1, 2, 3, 4, 5].
    #     """
    #     # 1. Define the formal parameters so that this method
    #     #    can be called recursively.
    #     # 2. Recursively call self._flatten and return the flat list.
    #     # 3. (FYI) The method name starts with an underscore to indicate that
    #     #    it is not intended to be called outside the class.
    #     # 4. Alternatively, put flatten as an inner function of
    #     #    find_subcategories.
    #     if type(L) == list:
    #         result = []
    #         for child in L:
    #             result.extend(self._flatten(child))
    #         return result
    #     else:
    #         return [L]
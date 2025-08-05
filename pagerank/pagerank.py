import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    # corpus = {'1': {'2'}, '2': {'1', '3'}, '3': {'4', '2', '5'}, '4': {'2', '1'}, '5': set()} 

    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # raise NotImplementedError
    transition_probality = {}
    total_pages = len(corpus)
    global_probability = (1 - damping_factor) / total_pages
    if len(corpus[page]) > 0:
        for key in corpus:
            if key in corpus[page]:
                transition_probality[key] = (damping_factor / len(corpus[page])) + global_probability
            else:
                transition_probality[key] = global_probability
    else:
        for key in corpus:
            transition_probality[key] = 1 / total_pages
    
    return transition_probality
        


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # raise NotImplementedError
    total_pages = [pages for pages in corpus]
    page_count = {}
    for page in total_pages:
        page_count[page] = 0

    current_page = ''
    for count in range(0, n):
        if count == 0:
            current_page = random.choice(total_pages)
            page_count[current_page] += 1
        else:
            transition_probability = transition_model(corpus, current_page, DAMPING)
            weights = []
            for page in total_pages:
                weights.append(transition_probability[page])
            current_page = random.choices(total_pages, weights = weights, k=1)[0]
            page_count[current_page] += 1
    
    pageRank = {}
    for page in page_count:
        pageRank[page] = (page_count[page] / n)
    
    return pageRank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # raise NotImplementedError
    pageRank = {}
    totalPages = len(corpus)
    for page in corpus:
        pageRank[page] = 1 / totalPages
    isContinue = True
    while isContinue:
        isContinue = False
        oldPageRank = pageRank.copy()
        for page in corpus:
            old = oldPageRank[page]
            pageRank[page] = (1 - damping_factor) / totalPages
            for key in corpus:
                if page in corpus[key]:
                    pageRank[page] += (damping_factor * (oldPageRank[key] / len(corpus[key])))
                if len(corpus[key]) == 0:
                    pageRank[page] += (damping_factor * (oldPageRank[key] / totalPages))
            if abs(old - pageRank[page]) >= 0.001:
                isContinue = True
    
    return pageRank


if __name__ == "__main__":
    main()
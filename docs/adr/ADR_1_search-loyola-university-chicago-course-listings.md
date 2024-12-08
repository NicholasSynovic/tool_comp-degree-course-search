# 1. Search Loyola University Chicago course listings

## Context

This application needs to be able to take a search query from the user and
return potential classes that could teach the user on the search query. These
courses need to come from acredited universities. As Loyola University Chicago
is the university that I am most familiar with, we will start the search process
there.

## Decision

We will search the course listings for COMP-related courses. The search results
will be parsed into a standard format and saved to disk initially.

## Consequences

This application will have to add universities manually. If it is possible to
implement an architecture that allows for easy extension and inclusion of
different universities, that would be best.

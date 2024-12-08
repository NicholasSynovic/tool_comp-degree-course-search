# 2. Implement an object to handle course listings

## Context

There are two types of data that we want to capture with this application from
each course search result:

1. The course listings per subject, and
1. The descriptions of each course

While some APIs return both in the same response, some do not. Furthermore,
responses are unique to each API. Thus, it would be beneficial to create an
object to store the relevant information in a strucuted, common format.

## Decision

Two classes will be created: `CourseListing` and `CourseDocument` to hold the
course listings and course descriptions respectfully.

The `CourseListing` object will hold all of the metadata pertaining the course
name, source, number, subject, and any extra information necessary for an API to
find the course document.

The `CourseDocument` object will have the course fully qualified name (i.e.,
SUBJECT NUMBER - NAME), the course description, and a URL to the course homepage
as well as a pointer to the relevant `CourseListing` object.

## Consequences

There should be a one-to-one mapping of `CourseListing` and `CourseDocument`.
This could justify merging the objects into a facade class called `Course` to
easily access the functionality of both.

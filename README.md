Pony Object-Relational Mapper
==================================

Pony is an object-relational mapper. The most interesting feature of Pony is its ability to write queries to the database using generator expressions. Pony works with entities which are mapped to a SQL database. Using generator syntax for writing queries allows the user to formulate very eloquent queries. It increases the level of abstraction and allows a programmer to concentrate on the business logic of the application. For this purpose Pony analyzes the abstract syntax tree of a generator and translates it to its SQL equivalent.

Following is an example of a query in Pony:

    select(p for p in Product if p.name.startswith('A') and p.cost <= 1000)

Pony translates queries to SQL using a specific database dialect. Currently Pony works with SQLite, MySQL, PostgreSQL and Oracle databases.

Pony ORM also include the ER Diagram Editor which is a great tool for prototyping. You can create your ER diagram online at [https://editor.ponyorm.com](https://editor.ponyorm.com), generate the database schema based on the diagram and start working with the database using declarative queries in seconds.

The package pony.orm.examples contains several examples.

Documenation is available at [https://docs.ponyorm.com](https://docs.ponyorm.com)
The documentation source is avaliable at [https://github.com/ponyorm/pony-doc](https://github.com/ponyorm/pony-doc), it is released under Apache 2.0 license.
Please create new documentation related issues [https://github.com/ponyorm/pony-doc/issues](https://github.com/ponyorm/pony-doc/issues) or make a pull request with your improvements.

We are looking forward to your comments and suggestions at our mailing list [http://ponyorm-list.ponyorm.com](http://ponyorm-list.ponyorm.com)

License
-----------

Pony ORM is released under multiple licenses, check [ponyorm.com](https://ponyorm.com/license-and-pricing.html) for more information.

Copyright (c) 2016 Pony ORM, LLC. All rights reserved.
team (at) ponyorm.com

Please send your questions, comments and suggestions to our mailing list [http://ponyorm-list.ponyorm.com](http://ponyorm-list.ponyorm.com)

# Requirements Definition
**Functionalities**

- **Entity administration.** The program shall let its administrator add, modify or remove any entity into the database.
- **Add new query.** The program shall let its administrator create a new query as long as it complies with data types and entity needs.
- **Remove new query.** The program shall let its administrator delete an existing query.
- **Update a query.** The program shall let its administrator update an existing query.
- **Search.** The program shall let its administrator search from the data in the database the following:
  - Search for the students under a teacher
  - Search for the teacher of a specific student
  - Search for the student inside a specific course
  - Search for the teacher of a specific course
- **Hours update.** Because on the main tasks of the system is to keep track of student hours worked inside their course workshop, the program shall let its administrator easily update a students amount of hours worked.
- **A student graduates/drops out.** The program shall let its administrator remove those students who graduate or drop out of a course.

**Non-Functionalities**

- **Reliability.**
- **Response time.** The program shall take no more than 5 seconds to respond single query searches and insertions, and no more than 10 seconds to respond to multi-query searches.
- **Maintenance.** Any type of system maintenance which requires the program to become unusable for any period of time shall not be performed during peak system use hours, namely, hours in which school personnel are working. This hours tend to be 7:00AM-4:00PM. Outside of these hours, system can be taken down for maintenance.
- **Legality.** The program administrator, as the program itself, shall comply with _Ley núm. 195 del año 2012: La Carta de Derechos del Estudiante de Puerto Rico._ Law which protects students right, including their information, and the right to not disclose it with only personal in direct relation with the student and the student itself.
- **Multi-platform functionality.** The program shall be able to be accessed from at least two popular browsers from the Windows OS or the Mac OS.
- **Performance.** The program shall be able to manage huge loads of data during processing.

*** Settings ***
Library  OracleDBLibrary

*** Variables ***
${HOST} =  localhost
${PORT} =  1521
${SID} =  ORCLCDB
${SERVICE NAME} =  ORCLPDB1
${USER} =  SYS
${PASSWORD} =  Oracle_123
${MODE} =  SYSDBA

${WRONG USER ERROR} =  DatabaseError: ORA-01017: invalid username/password; logon denied
${WRONG PASSWORD ERROR} =  DatabaseError: ORA-01017: invalid username/password; logon denied
${WRONG HOST ERROR} =  OperationalError: DPY-6005: cannot connect to database
${WRONG PORT ERROR} =  OperationalError: DPY-6005: cannot connect to database
${WRONG SID ERROR} =  OperationalError: DPY-6005: cannot connect to database
${WRONG SERVICE NAME ERROR} =  OperationalError: DPY-6005: cannot connect to database
${WRONG MODE ERROR} =  DatabaseError: ORA-01031: insufficient privileges

*** Test Cases ***
CONNECT TO ORACLE DATABASE WITH SID SUCCESSFULLY
    ${DSN} =  ORACLE MAKEDSN  host=${HOST}  port=${PORT}  sid=${SID}
    ORACLE CONNECT  user=${USER}  password=${PASSWORD}  dsn=${DSN}  mode=${MODE}
    ${CONNECTION STATUS} =  ORACLE CONNECTION PING
    SHOULD BE EQUAL  ${CONNECTION STATUS}  ${NONE}
    ORACLE CONNECTION CLOSE

CONNECT TO ORACLE DATABASE WITH SERVICE NAME SUCCESSFULLY
    ${DSN} =  ORACLE MAKEDSN  host=${HOST}  port=${PORT}  service_name=${SERVICE NAME}
    ORACLE CONNECT  user=${USER}  password=${PASSWORD}  dsn=${DSN}  mode=${MODE}
    ${CONNECTION STATUS} =  ORACLE CONNECTION PING
    SHOULD BE EQUAL  ${CONNECTION STATUS}  ${NONE}
    ORACLE CONNECTION CLOSE

CONNECT TO ORACLE DATABASE WITH WRONG USER FAILURE
    ${DSN} =  ORACLE MAKEDSN  host=${HOST}  port=${PORT}  sid=${SID}
    RUN KEYWORD AND EXPECT ERROR  STARTS:${WRONG USER ERROR}  ORACLE CONNECT  user=ADMIN  password=${PASSWORD}  dsn=${DSN}  mode=${MODE}

CONNECT TO ORACLE DATABASE WITH WRONG PASSWORD FAILURE
    ${DSN} =  ORACLE MAKEDSN  host=${HOST}  port=${PORT}  sid=${SID}
    RUN KEYWORD AND EXPECT ERROR  STARTS:${WRONG PASSWORD ERROR}  ORACLE CONNECT  user=${USER}  password=ORACLE_456  dsn=${DSN}  mode=${MODE}

CONNECT TO ORACLE DATABASE WITH WRONG HOST FAILURE
    ${DSN} =  ORACLE MAKEDSN  host=remotehost  port=${PORT}  sid=${SID}
    RUN KEYWORD AND EXPECT ERROR  STARTS:${WRONG HOST ERROR}  ORACLE CONNECT  user=${USER}  password=${PASSWORD}  dsn=${DSN}  mode=${MODE}

CONNECT TO ORACLE DATABASE WITH WRONG PORT FAILURE
    ${DSN} =  ORACLE MAKEDSN  host=${HOST}  port=2348  sid=${SID}
    RUN KEYWORD AND EXPECT ERROR  STARTS:${WRONG PORT ERROR}  ORACLE CONNECT  user=${USER}  password=${PASSWORD}  dsn=${DSN}  mode=${MODE}

CONNECT TO ORACLE DATABASE WITH WRONG SID FAILURE
    ${DSN} =  ORACLE MAKEDSN  host=${HOST}  port=${PORT}  sid=ORCLCSID
    RUN KEYWORD AND EXPECT ERROR  STARTS:${WRONG SID ERROR}  ORACLE CONNECT  user=${USER}  password=${PASSWORD}  dsn=${DSN}  mode=${MODE}

CONNECT TO ORACLE DATABASE WITH WRONG SERVICE NAME FAILURE
    ${DSN} =  ORACLE MAKEDSN  host=${HOST}  port=${PORT}  service_name=ORCLPDB2
    RUN KEYWORD AND EXPECT ERROR  STARTS:${WRONG SERVICE NAME ERROR}  ORACLE CONNECT  user=${USER}  password=${PASSWORD}  dsn=${DSN}  mode=${MODE}

CONNECT TO ORACLE DATABASE WITH WRONG MODE FAILURE
    ${DSN} =  ORACLE MAKEDSN  host=${HOST}  port=${PORT}  sid=${SID}
    RUN KEYWORD AND EXPECT ERROR  STARTS:${WRONG MODE ERROR}  ORACLE CONNECT  user=${USER}  password=${PASSWORD}  dsn=${DSN}  mode=SYSRAC

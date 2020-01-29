#****************************************************************************
#   GST REGISTRATION TYPE
#****************************************************************************
GST_REG_TYPE = (
    (0, 'Not Applicable'),
    (1, 'GST Registered-Regular'),
    (2, 'GST Registered-Composition,'),
    (3, 'GST unregistered'),
    (4, 'Consumer'),
    (5, 'Overseas'),
    (6, 'SEZ'),
    (7, 'Deemed Exports -EOU’s, STP’s , EHTP’s etc'),
)

#****************************************************************************
#   RECORD STATUS CODES
#****************************************************************************
IS_TRUE = ((True, 'YES'), (False, 'NO'))

#****************************************************************************
#   ORGANIZATION TYPE
#****************************************************************************
ORGANIZATION_TYPE = (
    (1, 'Individual'),
    (2, 'Proprietorship'),
    (3, 'LLP'),
    (4, 'Partnership'),
    (5, 'Trust'),
    (6, 'Gvt Organisation'),
)

#****************************************************************************
#   
#****************************************************************************

SALUTATIONS = (
    (0, 'Mr.'),
    (0, 'Mrs.'),
    (0, 'Miss'),
    (0, 'Dr.'),
    (0, 'Ms.'),
    (0, 'Prof.'),
    (0, 'Rev.'),
    (0, 'Lady'),
    (0, 'Sir'),
    (0, 'Capt.'),
    (0, 'Major'),
    (0, 'Lt.-Col.'),
    (0, 'Col.'),
    (0, 'Lady'),
    (0, 'Lt.-Cmdr.'),
    (0, 'The Hon.'),
    (0, 'Cmdr.'),
    (0, 'Flt. Lt.'),
    (0, 'Brgdr.'),
    (0, 'Judge'),
    (0, 'Lord'),
    (0, 'The Hon. Mrs'),
    (0, 'Wng. Cmdr.'),
    (0, 'Group Capt.'),
    (0, 'Rt. Hon. Lord'),
    (0, 'Revd. Father'),
    (0, 'Revd Canon'),
    (0, 'Maj.-Gen.'),
    (0, 'Air Cdre.'),
    (0, 'Viscount'),
    (0, 'Dame'),
    (0, 'Rear Admrl.')
)

#============================================================================
#
#
CUSTOMER_TYPE = (
    (1, 'CUSTOMER'),
    (2, 'VENDOR'),
    (3, 'EMPLOYEE'),
    (4, 'OTHERS'),
)

IS_SUB_CUSTOMER = (
    (1, 'Parent Customer'),
    (2, 'Bill With Parent'),
    (3, 'Bill with Customer'),
)
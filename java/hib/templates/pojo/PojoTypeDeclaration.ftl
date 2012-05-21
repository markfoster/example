/**
*   Data access object representing a ${pojo.getDeclarationName()}.
*
*   @author matth
*   @version $Rev: 2 $
*/
<#include "Ejb3TypeDeclaration.ftl"/>
${pojo.getClassModifiers()} ${pojo.getDeclarationType()} ${pojo.getDeclarationName()} ${pojo.getExtendsDeclaration()} ${pojo.getImplementsDeclaration()}

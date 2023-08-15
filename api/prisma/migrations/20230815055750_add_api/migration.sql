-- CreateTable
CREATE TABLE "Preview" (
    "id" TEXT NOT NULL,
    "authorID" BIGINT NOT NULL,
    "content" TEXT NOT NULL,

    CONSTRAINT "Preview_pkey" PRIMARY KEY ("id")
);

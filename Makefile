db-generate:
	@echo "🔄 Generating Prisma Client..."
	uv run prisma generate --schema=backend/src/db/prisma/schema.prisma

db-push:
	@echo "🚀 Pushing schema to database..."
	uv run prisma db push --schema=backend/src/db/prisma/schema.prisma

db-migrate: db-generate db-push
	@echo "✅ Database migration complete!"